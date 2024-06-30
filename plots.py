import os
import matplotlib.pyplot as plt

def plot_tax(taxes_groups,model_data,model_styles,plots_directory,title,variable,models):

    """
        Generate and save a plot for a specified tax-related variable across different model groups.

        This function creates a plot for the specified variable, using the data from the models defined
        in the taxes_groups. The plot is then saved into the specified directory.

        Args:
            taxes_groups (dict): A dictionary containing model groups related to taxes.
            model_data (dict): A dictionary containing model data for each model.
            model_styles (dict): A dictionary containing plot styles for each model.
            plots_directory (str): The path to the directory where the plot should be saved.
            title (str): The title for the plot.
            variable (str): The variable to plot.
            models (dict): A dictionary containing the model objects.

        Returns:
            None
    """
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_title(f'{title}')
    for model_key in taxes_groups['models']:
        if model_key in model_data:
            model_array = model_data[model_key]
            index = models[model_key]['variables'].index(variable)
            data = model_array[:35, index]
            style = model_styles[model_key]
            plot_style = style.copy()
            label = plot_style.pop('label')
            ax.plot(data, **plot_style, label=label)
    ax.legend()
    plt.savefig(os.path.join(plots_directory, f'{variable}.png'))
    plt.close(fig)



def plot_appendix(group1, group2, group3,model_groups,model_data,model_styles,variable_title_dict,plots_directory3,models):

    """
      Generate and save appendix plots for specified variable groups and models.

      This function creates a set of subplots for each group of variables and model combinations,
      then saves the generated plots into a specified directory.

      Args:
          group1 (tuple): The first group of variables to plot.
          group2 (tuple): The second group of variables to plot.
          group3 (tuple): The third group of variables to plot.
          model_groups (list): A list of dictionaries containing model groups to plot.
          model_data (dict): A dictionary containing model data for each model.
          model_styles (dict): A dictionary containing plot styles for each model.
          variable_title_dict (dict): A dictionary mapping variables to their descriptive titles.
          plots_directory3 (str): The path to the directory where plots should be saved.
          models (dict): A dictionary containing the model objects.

      Returns:
          None
    """

    legend_handles_all = {}
    legend_labels_all = {}
    
    for group_index, group in enumerate([group1, group2, group3], start=1):
        for model_key in model_groups[-1]['models']:
            fig, axs = plt.subplots(5, 3, figsize=(15, 15))

            for i, v in enumerate(group):
                ax = axs.flatten()[i]
                model_array = model_data[model_key]
                index = models[model_key]['variables'].index(v)
                data = model_array[:35, index]
                style = model_styles[model_key]
                plot_style = style.copy()
                label = plot_style.pop('label')
                line, = ax.plot(data, **plot_style, label=label)

                if not label.startswith('_'):
                    if label not in legend_handles_all:
                        legend_handles_all[label] = line
                        legend_labels_all[label] = label
                    else:

                        legend_handles_all[label] = line

                ax.set_title(variable_title_dict.get(v, v))

            fig.tight_layout()
            plt.savefig(os.path.join(plots_directory3, f'appendix{group_index}_model{model_key}_part.png'))  # Save figure for each model
            plt.close(fig)


def plot_ar(mod_lsls,x,plots_directory2):

    """
      Generate and save a plot for the AR(1) process of government spending.

      This function creates a plot showing the AR(1) process of government spending for the first 50 periods,
      then saves the plot into the specified directory.

      Args:
          mod_lsls (dict): The model object for the lump-sum tax in both countries model.
          x (ndarray): The array containing the model's time path data.
          plots_directory2 (str): The path to the directory where the plot should be saved.

      Returns:
          None
    """
    fig = plt.figure()
    plt.title('Government Spending AR1')
    plt.plot(x[:50, mod_lsls['variables'].index('gH')])
    plt.savefig(os.path.join(plots_directory2, f'gov_ar1.png'))
    plt.close(fig)

def plot_clean(group1_clean,group2_clean,model_groups,model_data,model_styles,variable_title_dict_clean,plots_directory2,models):

    """
       Generate and save clean plots for specified variable groups and models with legends.

       This function creates a set of subplots for each group of clean variables and model combinations,
       adds a legend, then saves the generated plots into a specified directory.

       Args:
           group1_clean (tuple): The first group of clean variables to plot.
           group2_clean (tuple): The second group of clean variables to plot.
           model_groups (list): A list of dictionaries containing model groups to plot.
           model_data (dict): A dictionary containing model data for each model.
           model_styles (dict): A dictionary containing plot styles for each model.
           variable_title_dict_clean (dict): A dictionary mapping clean variables to their descriptive titles.
           plots_directory2 (str): The path to the directory where plots should be saved.
           models (dict): A dictionary containing the model objects.

       Returns:
           None
    """

    legend_handles_all = {}
    legend_labels_all = {}
    for group_index, group in enumerate([group1_clean, group2_clean], start=1):

        fig, axs = plt.subplots(4, 3, figsize=(16.54, 23.38))

        for i, v in enumerate(group):
            ax = axs.flatten()[i]
            for model_key in model_groups[-1]['models']:
                model_array = model_data[model_key]
                index = models[model_key]['variables'].index(v)
                data = model_array[:35, index]
                style = model_styles[model_key]
                plot_style = style.copy()
                label = plot_style.pop('label')
                line, = ax.plot(data, **plot_style, label=label)

                if not label.startswith('_'):
                    if label not in legend_handles_all:
                        legend_handles_all[label] = line
                        legend_labels_all[label] = label
                    else:
                        legend_handles_all[label] = line

            ax.set_title(variable_title_dict_clean.get(v, v))


        legend_ax = fig.add_subplot(111, frame_on=False)
        legend_ax.xaxis.set_visible(False)
        legend_ax.yaxis.set_visible(False)


        handles = [handle for label, handle in legend_handles_all.items()]
        labels = [label for label, handle in legend_handles_all.items()]

        legend_ax.legend(handles=handles, labels=labels, loc='lower center', bbox_to_anchor=(0.5, -0.2),
                         fontsize='large')

        fig.tight_layout()

        fig.savefig(os.path.join(plots_directory2, f'plot_with_legend_group_{group_index}.png'))

        plt.close()