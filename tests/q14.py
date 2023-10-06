test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Hmmm, your `b`` variable looks incorrect.
          >>> np.isclose(b_for_Q14, epo_2, atol=2)
          True

          """,
          'hidden': False,
          'locked': False
        },

                {
          'code': r"""
          >>> # Hmmm, your `c`` variable looks incorrect.
          >>> np.isclose(c_for_Q14, tni_2, atol=2)
          True

          """,
          'hidden': False,
          'locked': False
        },

                        {
          'code': r"""
          >>> # Hmmm, the contents of your `errors` vector looks incorrect.
          >>>  np.allclose(errors_for_Q14, tester_4 - (tni_2 + tni_2 - tni_2 + epo_2*0 + tester_3*0 + epo_2*tester_3 + tester_3*0), atol=2)
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
