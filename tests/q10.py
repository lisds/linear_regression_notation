test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Hmmm, that isn't correct. You may want to revist the textbook page.
          >>> np.allclose(recreate_y_values(x, b, c, errors), y)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Oh dear - did you use the original y variable?
          >>> # I've sneakily make a test for that!
          >>> _y = y
          >>> del y
          >>> np.allclose(recreate_y_values(x, b, c, errors), _y)
          True
          >>> y = _y
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
