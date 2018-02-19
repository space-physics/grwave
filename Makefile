
grwave.exe: src/grwave.for
	$(FC) $^ -o $@
	
clean:
	$(RM) grwave.exe
