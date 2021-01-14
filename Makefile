CXX = g++
CPPFLAGS = -std=c++14 -Wall -g -MMD -MP -fPIC 

check:
	python3 -m pylint --disable=R,C src/*.py



build/filter.so: src/filter.cc src/filter_cwrap.cc
	mkdir -p build
	$(CXX) $(CPPFLAGS) -shared -o build/filter.so $^
