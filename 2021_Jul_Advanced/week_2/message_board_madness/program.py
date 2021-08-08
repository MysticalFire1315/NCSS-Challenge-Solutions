#! 21 min 35 sec
#! #1 passed all tests

def author_rankings(thread_list):
  # TODO: Determine (author, upvotes, ranking) over all threads.
  # Initialise a dict to store authors and upvotes
  author_list = {}
  
  # Add authors and upvotes to dict
  for thread in thread_list:
    # Problem does not ask for title or tags, so those can be ignored
    for post in thread['posts']:
      author_list = process_post(author_list, post)
  
  # Determine ranking for each author
  rankings = []
  for author, upvotes in author_list.items():
    rankings.append(tuple([author, upvotes, forum_ranking(upvotes)]))
  
  # Sort rankings by author, then total upvotes (highest to lowest)
  rankings.sort(key=lambda pair: pair[0])
  rankings.sort(key=lambda pair: pair[1], reverse=True)
  return rankings

def process_post(author_list, post):
  """ Process a post => modify author_list to match """
  # Problem does not ask for content, so that can be ignored
  try:
    author_list[post['author']] += post['upvotes']
  except:
    # Author not in author_list
    author_list[post['author']] = post['upvotes']
  
  # Return modified author_list
  return author_list
  
def forum_ranking(total_upvotes):
  """ Determine the Forum Ranking based on Total Upvotes """
  if total_upvotes == 0:
    return 'Insignificantly Evil'
  elif total_upvotes < 20:
    return 'Cautiously Evil'
  elif total_upvotes < 100:
    return 'Justifiably Evil'
  elif total_upvotes < 500:
    return 'Wickedly Evil'
  elif total_upvotes >= 500:
    return 'Diabolically Evil'

if __name__ == '__main__':
  # Example calls to your function.
  print('Example 1')
  report = author_rankings([
      {
          'title': 'Invade Manhatten, anyone?',
          'tags': ['world-domination', 'hangout'],
          'posts': [
              {
                  'author': 'Mr. Sinister',
                  'content': "I'm thinking 9 pm?",
                  'upvotes': 2,
              },
              {
                  'author': 'Mystique',
                  'content': "Sounds fun!",
                  'upvotes': 0,
              },
              {
                  'author': 'Magneto',
                  'content': "I'm in!",
                  'upvotes': 0,
              },
          ],
      }
    ])
  print(report == [
    ('Mr. Sinister', 2, 'Cautiously Evil'),
    ('Magneto', 0, 'Insignificantly Evil'),
    ('Mystique', 0, 'Insignificantly Evil')
  ])
  
  print('Example 2')
  report = author_rankings([
    {
      'title': 'Invade Manhattan, anyone?',
      'tags': ['world-domination', 'hangout'],
      'posts': [
        {
          'author': 'Mr. Sinister',
          'content': "I'm thinking 9 pm?",
          'upvotes': 2,
        }
      ]
    },
    {
      'title': 'Interested in a weekly meetup?',
      'tags': ['introductions', 'hangout'],
      'posts': [
        {
          'author': 'Mystique',
          'content': "Sounds fun!",
          'upvotes': 0,
        },
      ],
      }
    ])
  
  print(report == [
    ('Mr. Sinister', 2, 'Cautiously Evil'), 
    ('Mystique', 0, 'Insignificantly Evil')
  ])
