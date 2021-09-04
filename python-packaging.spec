%global debug_package %{nil}

Name: python-packaging
Epoch: 100
Version: 21.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Core utilities for Python packages
License:  Apache-2.0
URL: https://github.com/pypa/packaging/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
python-packaging provides core utilities for Python packages like
utilities for dealing with versions, specifiers, markers etc.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-packaging
Summary: Core utilities for Python packages
Requires: python3
Requires: python3-pyparsing >= 2.0.2
Provides: python3-packaging = %{epoch}:%{version}-%{release}
Provides: python3dist(packaging) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-packaging = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(packaging) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-packaging = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(packaging) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-packaging
python-packaging provides core utilities for Python packages like
utilities for dealing with versions, specifiers, markers etc.

%files -n python%{python3_version_nodots}-packaging
%license LICENSE
%{python3_sitelib}/packaging*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-packaging
Summary: Core utilities for Python packages
Requires: python3
Requires: python3-pyparsing >= 2.0.2
Provides: python3-packaging = %{epoch}:%{version}-%{release}
Provides: python3dist(packaging) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-packaging = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(packaging) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-packaging = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(packaging) = %{epoch}:%{version}-%{release}

%description -n python3-packaging
python-packaging provides core utilities for Python packages like
utilities for dealing with versions, specifiers, markers etc.

%files -n python3-packaging
%license LICENSE
%{python3_sitelib}/packaging*
%endif

%changelog
