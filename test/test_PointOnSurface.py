import package.PointOnSurface


def test():
    input_feature = {"geometry": {"coordinates": [[[[139.709874813, 35.678910056], [139.709823467, 35.678944327], [139.709689235, 35.679033921], [139.70985927, 35.679196658], [139.709988371, 35.679110078], [139.709993293, 35.679106775], [139.710041465, 35.679074474], [139.709874813, 35.678910056]]]], "type": "MultiPolygon"}, "properties": {}, "type": "Feature"}
    output_feature = {"geometry": {"coordinates": [[[[139.709874813, 35.678910056], [139.709823467, 35.678944327], [139.709689235, 35.679033921], [139.70985927, 35.679196658], [139.709988371, 35.679110078], [139.709993293, 35.679106775], [139.710041465, 35.679074474], [139.709874813, 35.678910056]]]], "type": "MultiPolygon"}, "properties": {"\u4ee3\u8868\u70b9\u7d4c\u5ea6": 139.709865667, "\u4ee3\u8868\u70b9\u7def\u5ea6": 35.679054197}, "type": "Feature"}
    assert package.PointOnSurface.PointOnSurface(input_feature) == output_feature
