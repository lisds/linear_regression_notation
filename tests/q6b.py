test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Hmmm, that isn't correct. You may want to revist the textbook page.
          >>> int(my_Q6B_answer) == np.round(np.sin(2 * np.pi * np.exp(1)) + np.log2(32) - np.sqrt(4) + np.log(5) - np.log(np.exp(1)) + np.exp(np.log10(100)) - np.log(np.exp(1)) - 6.18)
          True

          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}