import pandas as pd
from flask import jsonify

from app.graphs import bp


# from flask_restplus import Api,Resource


@bp.route('/bar_line', methods=['GET', 'POST'])
def bar_line():
    return_value = [
        -0.05964552, -0.00162261, 0.02375511, -0.0750799,
        0.01890229, 0.01890229, 0.01890229, -0.05573341,
        0.004828, -0.03047185, 0.0253638, -0.03704443
    ]

    return_value = pd.Series(return_value * 100).map(lambda x: round(x, 2)).tolist()

    emv_value = [9.26661123e+08, 9.25157511e+08, 9.47134725e+08, 8.76023947e+08,
                 8.92582803e+08, 8.92582803e+08, 8.92582803e+08, 8.42836124e+08,
                 8.46905339e+08, 8.21098570e+08, 8.41924753e+08, 8.10736130e+08]

    payload = {
        'category': pd.date_range(
            start='2018-01-02', periods=12, freq='D'
        ).map(lambda x: x.strftime('%Y-%m-%d')).to_list(),
        'data': list(zip(emv_value, return_value))
    }

    return jsonify(payload)
