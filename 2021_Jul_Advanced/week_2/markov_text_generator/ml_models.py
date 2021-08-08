# Any Machine Learning models used is created here

class MarkovModel(object):
  """ A Markov Model """
  
  # Set "private" variables
  @property
  def model(self):
    return self._model
  
  @model.setter
  def model(self, new_model):
    self._model = new_model
  
  def __init__(self):
    pass
  
  def fit(self, text):
    """
    Fit model to an array of texts. Note that this will also use '.' as a token.
    
    :param text: An array of texts to create model from.
    :type text: arr
    """
    # Create model with first item
    model = {}
    
    # Loop through array of texts to add each text to model
    for string in text:
      # Convert text to array of lowercase words
      string = string.lower().split()

      # Loop through text array to identify and store bigrams
      for index in range(len(string)):
        try:
          model[string[index]].append(string[index+1])
        except KeyError:
          # Word not in model yet
          try:
            model[string[index]] = [string[index+1]]
          except IndexError:
            # If index error, that means word is there but nothing following
            # Add empty arr
            model[string[index]] = []
        except IndexError:
          # If index error that means word is there, but nothing following.
          pass
    
    # Save to instance's model
    self.model = model