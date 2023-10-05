test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your `y_hat` variable does not contain the correct values.
          >>> # did you use the correct formula from the textbook page?
          >>> np.allclose(y_hat, [45.39228296, 42.6977492 , 53.47588424, 37.30868167, 45.39228296, 56.17041801, 53.47588424, 48.08681672], atol=1e-2)
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
