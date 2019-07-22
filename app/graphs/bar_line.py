import pandas as pd
from flask import jsonify, request

from app.api.errors import error_response
from app.graphs import bp


# import numpy as np


# from flask_restplus import Api,Resource


@bp.route('/bar_line', methods=['GET', 'POST'])
def bar_line():
    _args = request.args

    if not _args:
        return_value = [
            -0.05964552, -0.00162261, 0.02375511, -0.0750799,
            0.01890229, 0.01890229, 0.01890229, -0.05573341,
            0.004828, -0.03047185, 0.0253638, -0.03704443
        ]

        # return_value = pd.Series(return_value * 100).map(lambda x: round(x, 2)).tolist()

        # emv_value = [9.26661123e+08, 9.25157511e+08, 9.47134725e+08, 8.76023947e+08,
        #              8.92582803e+08, 8.92582803e+08, 8.92582803e+08, 8.42836124e+08,
        #              8.46905339e+08, 8.21098570e+08, 8.41924753e+08, 8.10736130e+08]

        vol_value = [0.04120189895341634,
                     0.0411296747187073,
                     -0.04146772251867945,
                     0.03320980525216389,
                     0.03133448438138365,
                     -0.029165401566960347,
                     0.029433396631199444,
                     0.030057759577343184,
                     -0.027866404141429157,
                     -0.02310100818597614,
                     0.0362744686507009,
                     0.029455136389356963]

        frame = pd.DataFrame.from_dict({'return': return_value, 'volatility': vol_value})
        frame.index = pd.date_range(start='2018-01-02', periods=12, freq='D'
                                    ).map(lambda x: x.strftime('%Y-%m-%d')).to_list()
        # frame['return'] *= 100
        frame['return'] = frame['return'].round(4)
        frame['volatility'] = frame['volatility'].round(4)
        frame.drop_duplicates(inplace=True)

        payload = {
            'category': frame.index.to_list(),
            'data': list(zip(frame.volatility.to_list(), frame['return'].to_list())),
            # 'bar': [min(frame.emv), max(frame.emv)],
            # 'line': [min(frame['return']), max(frame['return'])]
        }

        return jsonify(payload)

    return error_response(404, 'to be continue...')
