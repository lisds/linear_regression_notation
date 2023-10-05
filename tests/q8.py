test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your `errors` variable does not contain the correct values.
          >>> # it looks like you might have subtracted in the wrong direction...
          >>> np.allclose(errors, [ 5.39228296, -6.3022508 , -5.52411576, -0.69131833,  2.39228296, 0.17041801,  1.47588424,  3.08681672], atol=1e-2)
          False

          """,
          'hidden': False,
          'locked': False
        },

                {
          'code': r"""
          >>> # Your `errors` variable does not contain the correct values.
          >>> np.allclose(errors, [-5.39228296,  6.3022508 ,  5.52411576,  0.69131833, -2.39228296, -0.17041801, -1.47588424, -3.08681672], atol=1e-2)
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
