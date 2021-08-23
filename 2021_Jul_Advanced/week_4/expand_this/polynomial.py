
class Polynomial:
  
  @property
  def terms(self):
    return sorted(self._terms, reverse=True, key=lambda term: term.get_power())
  
  @terms.setter
  def terms(self, new_terms):
    self._terms = new_terms
  
  @property
  def degree(self):
    return max([term.get_power() for term in self.terms])
  
  def __init__(self, terms, pronumeral='x'):
    self.terms = terms
    self._pronumeral = pronumeral
  
  def __repr__(self):
    # Sort terms by term's individual power
    terms_to_join = []
    for term in self.terms:
      if term.get_coeff() != 0:
        terms_to_join.append(term)
        
    to_return = ' + '.join([str(term) for term in terms_to_join])
    to_return = to_return.replace('+ -', '- ')
    to_return = to_return.replace(self.get_pronumeral() + '^0', '')
    to_return = to_return.replace('^1', '')
    to_return = to_return.replace('1' + self.get_pronumeral(), self.get_pronumeral())
    
    return to_return
  
  def __str__(self):
    # Sort terms by term's individual power
    terms_to_join = []
    for term in self.terms:
      if term.get_coeff() != 0:
        terms_to_join.append(term)
        
    to_return = ' + '.join([str(term) for term in terms_to_join])
    to_return = to_return.replace('+ -', '- ')
    to_return = to_return.replace(self.get_pronumeral() + '^0', '')
    to_return = to_return.replace('^1', '')
    to_return = to_return.replace('1' + self.get_pronumeral(), self.get_pronumeral())
    
    return to_return
  
  def __add__(self, other):
    if self.degree > other.degree:
      highest_degree = self.degree
    else:
      highest_degree = other.degree
    
    new_polynomial_terms = []
    
    for power in range(highest_degree + 1):
      self_term_index = self._find_power_index(self.terms, power)
      other_term_index = other._find_power_index(other.terms, power)
      
      if self_term_index is not None:
        new_term = self.terms[self_term_index]
      else:
        new_term = Term(0, self.get_pronumeral(), power)
      
      if other_term_index is not None:
        new_term += other.terms[other_term_index]
      else:
        new_term += Term(0, self.get_pronumeral(), power)
      
      new_polynomial_terms.append(new_term)
    
    return Polynomial(new_polynomial_terms, self.get_pronumeral())
  
  def __sub__(self, other):
    if self.degree > other.degree:
      highest_degree = self.degree
    else:
      highest_degree = other.degree
    
    new_polynomial_terms = []
    
    for power in range(highest_degree + 1):
      self_term_index = self._find_power_index(self.terms, power)
      other_term_index = other._find_power_index(other.terms, power)
      
      if self_term_index is not None:
        new_term = self.terms[self_term_index]
      else:
        new_term = Term(0, self.get_pronumeral(), power)
      
      if other_term_index is not None:
        new_term -= other.terms[other_term_index]
      else:
        new_term -= Term(0, self.get_pronumeral(), power)
      
      new_polynomial_terms.append(new_term)
    
    return Polynomial(new_polynomial_terms, self.get_pronumeral())
  
  def __mul__(self, other):
    new_polynomial_terms = []
    
    for self_term in self.terms:
      individual_multiplication_terms = []
      for other_term in other.terms:
        individual_multiplication_terms.append(self_term * other_term)
      new_polynomial_terms.append(Polynomial(individual_multiplication_terms, self.get_pronumeral()))
    return_polynomial = Polynomial([Term(0, self.get_pronumeral(), 0)], self.get_pronumeral())
    
    for polynomial in new_polynomial_terms:
      return_polynomial += polynomial
    
    return return_polynomial
  
  def __pow__(self, other):
    if other.terms[0].get_power() != 0:
      raise ValueError(f'{other.terms[0].get_power()}')
      
    new_poly = self
    for index in range(other.terms[0].get_coeff() - 1):
      new_poly *= self
    
    return new_poly
  
  def _find_power_index(self, terms, power):
    for index in range(len(terms)):
      if terms[index].get_power() == power:
        return index
    return None
  
  def get_pronumeral(self):
    return self._pronumeral


class Term:
  def __init__(self, coefficient=1, pronumeral='x', power=1):
    self._coeff = coefficient
    self._pronum = pronumeral
    self._power = power
  
  def get_coeff(self):
    return self._coeff
  
  def get_pronum(self):
    return self._pronum
  
  def get_power(self):
    return self._power
  
  def __str__(self):
    return f'{self.get_coeff()}{self.get_pronum()}^{self.get_power()}'
  
  def __repr__(self):
    return f'{self.get_coeff()}{self.get_pronum()}^{self.get_power()}'
  
  def __add__(self, other):
    """
    Returns the addition (+) of two :class:`Term`s. Note that terms can only
    be added if pronumerals and powers are the same OR both powers are 0.
    """
    # Check that powers are the same
    if self.get_power() == other.get_power():
      # Check pronumerals are also the same, or power =0 (int)
      if self.get_pronum() == other.get_pronum() or self.get_power() == 0:
        return Term(
          coefficient = self.get_coeff() + other.get_coeff(),
          pronumeral = self.get_pronum(),
          power = self.get_power()
        )
    else:
      raise TypeError
  
  def __sub__(self, other):
    """
    Returns the subtraction (-) of two :class:`Term`s. Note that terms can only
    be subtracted if pronumerals and powers are the same.
    """
    # Check that powers are the same
    if self.get_power() == other.get_power():
      # Check pronumerals are also the same, or power =0 (int)
      if self.get_pronum() == other.get_pronum() or self.get_power() == 0:
        return Term(
          coefficient = self.get_coeff() - other.get_coeff(),
          pronumeral = self.get_pronum(),
          power = self.get_power()
        )
    else:
      raise TypeError
  
  def __mul__(self, other):
    """
    Returns the multiplication (*) of two :class:`Term`s. Note that terms can
    only be multiplied if pronumerals are the same.
    """
    if self.get_pronum() == other.get_pronum():
      return Term(
        coefficient = self.get_coeff() * other.get_coeff(),
        pronumeral = self.get_pronum(),
        power = self.get_power() + other.get_power()
      )
    else:
      raise TypeError
