def test_xflr_dat_to_dataframe():
    from post_processing import xflr_dat_to_dataframe
    frame = xflr_dat_to_dataframe('test/sample_plane_analysis.txt')
    # This test would only world if the file is perfectly parsed..
    assert frame['QInf'].iloc[11] == 9.6519

def test_window_edit_section_index():
    from window_edit import section_index
    pass

