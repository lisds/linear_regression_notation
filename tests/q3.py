test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
                      {
        'code': r"""
        >>> # It looks like you have expressed each value as a PROPORTION of the total score, not as a PERCENTAGE of the total score.
        >>> # Hint: try multiplying each value by 100 to convert them to percentages.
        >>> np.allclose(x_as_percentage, [0.7 , 0.65, 0.85, 0.55, 0.7 , 0.9 , 0.85, 0.75])
        False
        """,
        'hidden': False,
        'locked': False
        },
        {
          'code': r"""
          >>> # `x_as_percentage` contains the wrong values!
          >>> np.allclose(x_as_percentage, [70., 65., 85., 55., 70., 90., 85., 75.])
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
