test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Hmmm, your `b`` variable looks incorrect.
          >>> np.isclose(b_for_Q12, 0.59, atol=2)
          True

          """,
          'hidden': False,
          'locked': False
        },

                {
          'code': r"""
          >>> # Hmmm, your `c`` variable looks incorrect.
          >>> np.isclose(c_for_Q12, 10.6, atol=2)
          True

          """,
          'hidden': False,
          'locked': False
        },

                        {
          'code': r"""
          >>> # Hmmm, the contents of your `errors` vector looks incorrect.
          >>>  np.allclose(errors_for_Q12, tester_2 - (10.6 + 10.6 - 10.6 + 0.59*0 + tester*0 + 0.59*tester + tester*0), atol=2)
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
