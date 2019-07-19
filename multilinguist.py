import requests
import json
import random

class Multilinguist:
  """This class represents a world traveller who knows 
  what languages are spoken in each country around the world
  and can cobble together a sentence in most of them
  (but not very well)
  """

  translatr_base_url = "http://bitmakertranslate.herokuapp.com"
  countries_base_url = "https://restcountries.eu/rest/v2/name"
  #{name}?fullText=true
  #?text=The%20total%20is%2020485&to=ja&from=en

  def __init__(self):
    """Initializes the multilinguist's current_lang to 'en'
    
    Returns
    -------
    Multilinguist
        A new instance of Multilinguist
    """
    self.current_lang = 'en'

  def language_in(self, country_name):
    """Uses the RestCountries API to look up one of the languages
    spoken in a given country

    Parameters
    ----------
    country_name : str
         The full name of a country.

    Returns
    -------
    bool 
        2 letter iso639_1 language code.
    """
    params = {'fullText': 'true'}
    response = requests.get(f"{self.countries_base_url}/{country_name}", params=params)
    json_response = json.loads(response.text)
    try:
      return json_response[0]['languages'][0]['iso639_1']
    except KeyError:
      return "Not Great"

  def travel_to(self, country_name):
    """Sets current_lang to one of the languages spoken
    in a given country

    Parameters
    ----------
    country_name : str
        The full name of a country.

    Returns
    -------
    str
        The new value of current_lang as a 2 letter iso639_1 code.
    """
    local_lang = self.language_in(country_name)
    self.current_lang = local_lang
    return self.current_lang

  def say_in_local_language(self, msg):
    """(Roughly) translates msg into current_lang using the Transltr API

    Parameters
    ----------
    msg : str
        A message to be translated.

    Returns
    -------
    str
        A rough translation of msg.
    """
    params = {'text': msg, 'to': self.current_lang, 'from': 'en'}
    response = requests.get(self.translatr_base_url, params=params)
    json_response = json.loads(response.text)
    try:
      return json_response['translationText']
    except KeyError:
      return "Also not great"

class MathGenuis(Multilinguist):

  def report_total(self, num_list):
    for number in num_list:
      summ = number =+ number
    return self.say_in_local_language(f'The total is {summ}')


class QuoteCollector(Multilinguist):

  def __init__(self):

    super().__init__()
    self.quotes = [] 
  

  def collecting_quotes(self, quote):
    self.quotes.append(quote)

  def selecting_random_quote(self):
    quote = self.say_in_local_language(random.choice(self.quotes))
    return quote
  
new_collector = QuoteCollector()
new_collector.travel_to("Japan")
new_collector.collecting_quotes("and then we had the bisque, yada yada yada")
new_collector.collecting_quotes("do or do not, there is no try")
new_collector.collecting_quotes("failing is not trying, all other outcomes are degrees of success")
print(new_collector.selecting_random_quote())



me = MathGenuis()
print(me.report_total([23,45,676,34,5778,4,23,5465]))
me.travel_to("India")
print(me.report_total([6,3,6,68,455,4,467,57,4,534]))
    
new_traveler = Multilinguist()
print(new_traveler.language_in('france'))
print(new_traveler.travel_to('england'))
print(new_traveler.say_in_local_language("what's going on here?"))