import fmm
model = fmm.MapMatcher("fmm_config.xml")
wkt = "LINESTRING (0.200812146892656 2.14088983050848,1.44262005649717 2.14879943502825,3.06408898305084 2.16066384180791,3.06408898305084 2.7103813559322,3.70872175141242 2.97930790960452,4.11606638418078 2.62337570621469)"
print model.match_geometry(wkt)
