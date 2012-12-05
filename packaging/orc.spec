Name:           orc
Version:        0.4.16
Release:        0
License:        BSD-3-Clause
Summary:        The Oil Runtime Compiler
Url:            http://code.entropywave.com/projects/orc/
Group:          Productivity/Multimedia/Other
Source:         http://code.entropywave.com/download/orc/%{name}-%{version}.tar.gz
BuildRequires:  libxslt-tools
BuildRequires:  pkg-config
Provides:       %{name}-devel = %{version}

%description
Orc is a library and set of tools for compiling and executing very simple
programs that operate on arrays of data.  The “language” is a generic
assembly language that represents many of the features available in SIMD
architectures, including saturated addition and subtraction, and many
arithmetic operations.

%package -n liborc
Summary:        The Oil Runtime Compiler Library
Group:          System/Libraries

%description -n liborc
Orc is a library and set of tools for compiling and executing very simple
programs that operate on arrays of data.  The “language” is a generic
assembly language that represents many of the features available in SIMD
architectures, including saturated addition and subtraction, and many
arithmetic operations.

%package doc
Summary:        The Oil Runtime Compiler Library - Documentation
Group:          Documentation/HTML

%description doc
Orc is a library and set of tools for compiling and executing very simple
programs that operate on arrays of data.  The “language” is a generic
assembly language that represents many of the features available in SIMD
architectures, including saturated addition and subtraction, and many
arithmetic operations.

%prep
%setup -q

%build
%configure \
    --disable-static \
    --disable-gtk-doc
make %{?_smp_mflags}
%check
%ifnarch %arm
make check
%endif

%install
%make_install
# These are some examples that seem not to make sense to be distributed
rm -rf %{buildroot}%{_libdir}/orc


%post -n liborc -p /sbin/ldconfig

%postun -n liborc -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/orc-bugreport
%{_bindir}/orcc
%{_includedir}/orc-0.4/
%{_libdir}/*.so
%{_libdir}/pkgconfig/orc-0.4.pc
%{_datadir}/aclocal/orc.m4

%files doc
%defattr(-,root,root)
%{_datadir}/gtk-doc/html/orc/

%files -n liborc
%defattr(-,root,root)
%{_libdir}/liborc*-0.4.so.*
