import copy

def dataframe_subset_combined(df, restrict_dict = {},
                              restrict_dict_floor = {},
                              restrict_dict_ceiling = {}):
  """
  Parameters
    see dataframe_subset_categorical, dataframe_subset_noncategorical
  """

  df1 = dataframe_subset_categorical(df, restrict_dict)

  return dataframe_subset_noncategorical(df1, restrict_dict_floor, restrict_dict_ceiling)
  

def dataframe_subset_categorical(df, restrict_dict = {}):
  """
  Parameters
    df : pandas dataframe
    restrict_dict : dict
      keys : names of df columns
      values : lists of column values to include
  """

  df1 = df

  for key in restrict_dict.keys():
    df1 = df1.loc[df[key].isin(restrict_dict[key])]

  return copy.deepcopy(df1)


def dataframe_subset_noncategorical(df, restrict_dict_floor = {},
                                    restrict_dict_ceiling = {}):
  """
  Parameters
    df : pandas dataframe
    restrict_dict_floor : dict
      keys : names of df columns
      values : float, subset minimum
    restrict_dict_ceiling : dict
      keys : names of df columns
      values : float, subset maximum
  """

  df1 = df

  for key in restrict_dict_floor.keys():
    df1 = df1.loc[df1[key] >= restrict_dict_floor[key]]

  for key in restrict_dict_ceiling.keys():
    df1 = df1.loc[df1[key] <= restrict_dict_ceiling[key]]

  return copy.deepcopy(df1)
  
    
