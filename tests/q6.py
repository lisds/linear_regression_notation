test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your parameter estimates are not correct. Did you perform a 
          >>> # linear regression using `x` as the predictor and `y` as the
          >>> # outcome?
          >>> (np.isclose(b,  2.69, atol=1e-2)) & (np.isclose(c,  7.66, atol=1e-2))
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