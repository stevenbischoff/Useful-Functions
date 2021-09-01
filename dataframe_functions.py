def dataframe_subset_categorical(df, restrict_dict = {}):
  """
  Parameters
    df : pandas dataframe
    restrict_dict : dict
      keys : names of columns of df
      values : lists of column values to include
  """

  import copy

  df1 = df

  for key in restrict_dict.keys():
    df1 = df1.loc[df[key].isin(restrict_dict[key])]

  return copy.deepcopy(df1)
    
