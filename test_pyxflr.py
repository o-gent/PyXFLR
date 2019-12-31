from post_processing import xflr_dat_to_dataframe

def test_xflr_dat_to_dataframe():
    frame = xflr_dat_to_dataframe('test/sample_plane_analysis.txt')
    # This test would only world if the file is perfectly parsed..
    assert frame['QInf'].iloc[11] == 9.6519