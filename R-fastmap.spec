#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fastmap
Version  : 1.1.0
Release  : 23
URL      : https://cran.r-project.org/src/contrib/fastmap_1.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fastmap_1.1.0.tar.gz
Summary  : Fast Data Structures
Group    : Development/Tools
License  : MIT
Requires: R-fastmap-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
store, stack, and queue. Environments are commonly used as key-value stores
    in R, but every time a new key is used, it is added to R's global symbol
    table, causing a small amount of memory leakage. This can be problematic in
    cases where many different keys are used. Fastmap avoids this memory leak
    issue by implementing the map using data structures in C++.

%package lib
Summary: lib components for the R-fastmap package.
Group: Libraries

%description lib
lib components for the R-fastmap package.


%prep
%setup -q -c -n fastmap
cd %{_builddir}/fastmap

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641012058

%install
export SOURCE_DATE_EPOCH=1641012058
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fastmap
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fastmap
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fastmap
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fastmap || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fastmap/DESCRIPTION
/usr/lib64/R/library/fastmap/INDEX
/usr/lib64/R/library/fastmap/LICENSE
/usr/lib64/R/library/fastmap/Meta/Rd.rds
/usr/lib64/R/library/fastmap/Meta/features.rds
/usr/lib64/R/library/fastmap/Meta/hsearch.rds
/usr/lib64/R/library/fastmap/Meta/links.rds
/usr/lib64/R/library/fastmap/Meta/nsInfo.rds
/usr/lib64/R/library/fastmap/Meta/package.rds
/usr/lib64/R/library/fastmap/NAMESPACE
/usr/lib64/R/library/fastmap/NEWS.md
/usr/lib64/R/library/fastmap/R/fastmap
/usr/lib64/R/library/fastmap/R/fastmap.rdb
/usr/lib64/R/library/fastmap/R/fastmap.rdx
/usr/lib64/R/library/fastmap/help/AnIndex
/usr/lib64/R/library/fastmap/help/aliases.rds
/usr/lib64/R/library/fastmap/help/fastmap.rdb
/usr/lib64/R/library/fastmap/help/fastmap.rdx
/usr/lib64/R/library/fastmap/help/paths.rds
/usr/lib64/R/library/fastmap/html/00Index.html
/usr/lib64/R/library/fastmap/html/R.css
/usr/lib64/R/library/fastmap/tests/testthat.R
/usr/lib64/R/library/fastmap/tests/testthat/helpers-fastmap.R
/usr/lib64/R/library/fastmap/tests/testthat/test-encoding.R
/usr/lib64/R/library/fastmap/tests/testthat/test-map.R
/usr/lib64/R/library/fastmap/tests/testthat/test-queue.R
/usr/lib64/R/library/fastmap/tests/testthat/test-serialize.R
/usr/lib64/R/library/fastmap/tests/testthat/test-shrink.R
/usr/lib64/R/library/fastmap/tests/testthat/test-stack.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fastmap/libs/fastmap.so
/usr/lib64/R/library/fastmap/libs/fastmap.so.avx2
/usr/lib64/R/library/fastmap/libs/fastmap.so.avx512
