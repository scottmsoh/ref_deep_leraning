import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel, PeftConfig
import torch
import os
import json
from datetime import datetime

@st.cache_resource
def load_model():
    try:
        # Check GPU 
        if not torch.cuda.is_available():
            st.error("GPU not available!")
            return None, None
            
        print("Loading model on GPU...")
        
        # BitsAndBytes configuration (GPU memory optimization)
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=False
        )
        
        # base model load
        base_model = AutoModelForCausalLM.from_pretrained(
            "microsoft/phi-2",
            quantization_config=bnb_config,
            device_map="auto",
            trust_remote_code=True
        )
        
        # tokenizer load
        tokenizer = AutoTokenizer.from_pretrained(
            "microsoft/phi-2",
            trust_remote_code=True
        )
        if not tokenizer.pad_token:
            tokenizer.pad_token = tokenizer.eos_token
        
        # fine-tuned model load
        model = PeftModel.from_pretrained(
            base_model,
            "ohmseok/ms_phi-2_finetune_finance",
        )
        
        model.eval()
        return model, tokenizer
        
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None, None

def generate_text(prompt, max_length=200, temperature=0.7):
    try:
        formatted_prompt = f"Below is an instruction that describes a task. ### Instruction: {prompt} ### Response:"
        
        inputs = tokenizer(
            formatted_prompt,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=max_length,
            return_attention_mask=True
        )
        
        # GPU configure
        inputs = {k: v.to('cuda') for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=max_length,
                temperature=temperature,
                num_beams=5,
                no_repeat_ngram_size=3,
                pad_token_id=tokenizer.pad_token_id,
                do_sample=True,
                early_stopping=True
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        response = response.split("### Response:")[-1].strip()
        
        return response
        
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
        return "Error generating response"

model, tokenizer = load_model()

base_dir = "./chat_sessions"
if not os.path.exists(base_dir):
    os.makedirs(base_dir)


def get_existing_sessions():
    sessions = []
    for file in os.listdir(base_dir):
        if file.endswith(".json"):
            sessions.append(file.replace(".json", ""))
    return sessions


def save_chat_history(chat_id, chat_history):
    with open(os.path.join(base_dir, f"{chat_id}.json"), "w") as f:
        json.dump(chat_history, f)


def load_chat_history(chat_id):
    file_path = os.path.join(base_dir, f"{chat_id}.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return []

def q_and_a_page():
    st.title("Financial Q&A Assistant")
    st.write("Ask me anything about finance and business!")

    if st.sidebar.button("⬅️ Back to Main", key="qa_back_to_main_sidebar"):
        st.session_state.page = "main"
    

    if "selected_chat" not in st.session_state:
        st.session_state.selected_chat = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.sidebar.title("Chat Sessions")

    
    existing_sessions = get_existing_sessions()
    if st.sidebar.button("New Chat", key="new_chat_button"):
        new_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.selected_chat = new_chat_id
        st.session_state.chat_history = []
        save_chat_history(new_chat_id, st.session_state.chat_history)

    
    for session in existing_sessions:
        if st.sidebar.button(session, key=f"session_button_{session}"):
            st.session_state.selected_chat = session
            st.session_state.chat_history = load_chat_history(session)

    
    if st.session_state.selected_chat:
        st.sidebar.markdown(f"**Current Chat:** {st.session_state.selected_chat}")

    
    header, main_content = st.columns([4, 1])
    
    with header:
        if model is not None:
            user_input = st.text_input("Your question:", key="user_input_field")
            if st.button("Send", key="send_button") and user_input:
                st.session_state.chat_history.append({"role": "user", "content": user_input})

                with st.spinner("AI is thinking..."):
                    ai_response = generate_text(
                        user_input, 
                        max_length=st.session_state.get('max_length', 200),
                        temperature=st.session_state.get('temperature', 0.7)
                    )
                    st.session_state.chat_history.append({"role": "ai", "content": ai_response})

                if st.session_state.selected_chat:
                    save_chat_history(st.session_state.selected_chat, st.session_state.chat_history)

            # chat history 
            st.subheader("Chat History")
            for chat in st.session_state.chat_history:
                role = "You" if chat["role"] == "user" else "AI"
                st.markdown(f"**{role}**: {chat['content']}")
                st.markdown("---")
        else:
            st.error("Model failed to load. Please check GPU availability.")

    
    with main_content:
        with st.expander("⚙️ Settings", expanded=False):
            st.write("Configure response generation:")
            st.session_state['max_length'] = st.slider(
                "Max Length", 50, 500, 200, 
                key="max_length_slider"
            )
            st.session_state['temperature'] = st.slider(
                "Temperature", 0.1, 1.0, 0.7, 
                key="temperature_slider"
            )

if __name__ == "__main__":
    q_and_a_page()