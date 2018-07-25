import delimited /Users/harry/Mus/reviews.csv, clear
graph drop _all 
drop if pitchfork == .
reg fantano pitchfork
mean(pitchfork)
mean(fantano)
histogram fantano, frequency normal saving(fantano, replace) 
histogram pitchfork, frequency normal saving(pitchfork, replace)
gr combine fantano.gph pitchfork.gph, col(1) iscale(1)
