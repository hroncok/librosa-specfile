Name:           python3-librosa
Version:        0.4.2
Release:        2%{?dist}
Summary:        A python package for music and audio analysis
License:        ISC
URL:            https://github.com/bmcfee/librosa
Source0:        https://github.com/bmcfee/librosa/archive/0.4.2.tar.gz

%define debug_package %{nil}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-numpydoc
BuildRequires:  python3-seaborn
BuildRequires:  python3-sphinx_rtd_theme

Requires:       python3-audioread
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-scikit-learn
Requires:       python3-matplotlib
Requires:       python3-joblib
Requires:       python3-decorator
Requires:       python3-six

%description
LibROSA is a python package for music and audio analysis. It provides the building blocks necessary to create music information retrieval systems.

%prep
%setup -q -n librosa-%{version}

%build
%py3_build

%install
%py3_install

%files -n %{name}
%doc README.md
%license LICENSE.md
%{python3_sitelib}/librosa/
%{python3_sitelib}/librosa-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Mar 09 2016 Dominika Krejci <dkrejci@redhat.com> - 0.4.2-2
- initial release
