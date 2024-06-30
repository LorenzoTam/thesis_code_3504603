from utils import initialize_data, run_models_with_shock,create_plot_directories
from plots import plot_appendix,plot_tax, plot_ar, plot_clean

if __name__ == "__main__":
    plots_directory,plots_directory2,plots_directory3=create_plot_directories()
    variable_title_dict,variable_title_dict_clean,variables, variables_clean, var_nameslab_clean, var_nameslab, model_styles, model_groups, taxes_groups, taxes,group1,group2,group3,group1_clean,group2_clean = initialize_data()
    model_data,models, mod_lsls, mod_lablab, mod_lslab, mod_labls, mod_FbiggerH, mod_HbiggerF=run_models_with_shock()
    plot_tax(taxes_groups[0], model_data, model_styles, plots_directory, 'Home Taxes', taxes[0],models)
    plot_tax(taxes_groups[1], model_data, model_styles, plots_directory, 'Foreign Taxes', taxes[1],models)
    plot_appendix(group1, group2, group3, model_groups, model_data, model_styles, variable_title_dict, plots_directory3,models)
    plot_ar(mod_lsls,model_data['mod_lsls'],plots_directory2)
    plot_clean(group1_clean, group2_clean, model_groups, model_data, model_styles, variable_title_dict_clean,plots_directory2,models)