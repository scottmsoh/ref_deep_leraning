

### Efficient Environment Setup Guide for Deep Learning Experiments

1. **Limitations of Jupyter Notebook**
   - Jupyter Notebook (.ipynb) is useful for interactive data analysis and experimentation, but writing code in .py scripts is essential to enhance the efficiency of deep learning experiments.
   - Especially for large-scale model training or tasks requiring long training times, .py scripts are more suitable.</br>

2. **Long Training Times**
   - Typically, deep learning experiments can take over 30 hours per epoch.</br>
   - Therefore, a stable and continuously running environment is necessary.</br>

3. **Utilizing Linux and Tmux**
   - Experiments are primarily conducted in a Linux environment or a Mac environment using Tmux via the command line.</br>
   - Using Tmux allows you to maintain sessions, run multiple tasks simultaneously, and reattach to sessions, making it ideal for long-running experiments.</br>

4. **Efficient Hyperparameter Tuning**
   - In multiple experiments, adjusting hyperparameters by modifying the .py file each time is inefficient.</br>
   - Thus, it is necessary to accept hyperparameters as command-line arguments.</br>

5. **Using ArgumentParser**
   - By using Python's `argparse` module to handle command-line arguments, hyperparameters can be adjusted efficiently.</br>
   - For example, you can specify hyperparameters on the command line like `train.py --learning_rate=1e-4`.</br>
