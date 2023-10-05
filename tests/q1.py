test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # your variable `x` is not a numpy array!
          >>> type(x) == np.ndarray
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Your vector vector `x` does not contain the correct values!
          >>> list(x) == [14, 13, 17, 11, 14, 18, 17, 15]
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
