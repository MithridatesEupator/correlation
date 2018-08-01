def covariance(chart, x_vars, y_vars):
    check = True
    for list in chart:
        for list_chart in chart:
            if len(list) != len(list_chart):
                raise ValueError("Each row must have same length!")
                check = False
    expectation_xy = 0
    expectation_x_y = 0
    if check:
        if len(y_vars) != len(chart[0]) or len(x_vars) != len(chart):
            raise ValueError("Check your X and Y values!")
        index = len(chart)
        j = 0;
        final = 0
        while j != index:
            index_list = len(chart[j])
            i = 0
            while i != index_list:
                final += x_vars[j] * y_vars_pass[i] * chart[j][i]
                i += 1
            j += 1
        expectation_xy = final
        final_x = 0
        final_y = 0
        final_x_2 = 0
        final_y_2 = 0
        j = 0;
        while j != index:
            index_list = len(chart[j])
            i = 0
            while i != index_list:
                final_x += x_vars[j] * chart[j][i]
                final_y += y_vars[i] * chart[j][i]
                final_x_2 += x_vars[j] ** 2 * chart[j][i]
                final_y_2 += y_vars[i] ** 2 * chart[j][i]
                i += 1
            j += 1
        return round((expectation_xy - final_x * final_y) / (final_x_2 * final_y_2), 2)

chart_pass = [[.1,0,.1,.2],
              [.0,.1,.2,.1],
              [.1,0,.1,0]]
x_vars_pass = [-2,4,5]
y_vars_pass = [0,2,4,6]
print(covariance(chart_pass, x_vars_pass, y_vars_pass))