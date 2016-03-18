Name:           librosa
Version:        0.4.2
Release:        1%{?dist}
Summary:        A python package for music and audio analysis
License:        ISC
URL:            https://github.com/bmcfee/librosa
Source0:        https://github.com/bmcfee/librosa/archive/0.4.2.tar.gz

%define debug_package %{nil}

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python3-devel

Requires:       python2-audioread
Requires:       python2-numpy
Requires:       python2-scipy
Requires:       python2-scikit-learn
Requires:       python2-matplotlib
Requires:       python2-joblib
Requires:       python2-decorator
Requires:       python2-six

Requires:       python3-audioread
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-scikit-learn
Requires:       python3-matplotlib
Requires:       python3-joblib
Requires:       python3-decorator
Requires:       python3-six

%description
LibROSA is a python package for music and audio analysis.
It provides the building blocks necessary to create music
information retrieval systems.

%package -n python2-librosa
Summary: Version for Python 2
%description -n python2-librosa
LibROSA is a python package for music and audio analysis.
It provides the building blocks necessary to create music
information retrieval systems.

%package -n python3-librosa
Summary: verion for Python 3
%description -n python3-librosa
LibROSA is a python package for music and audio analysis.
It provides the building blocks necessary to create music
information retrieval systems.

%prep
%setup -q -n librosa-%{version}

# Find all *.py files with the exact line '#!/usr/bin/env python' and for each
# such file replace the line with nothing (if it's the 1st line).
grep -ilrx librosa -e '#!/usr/bin/env python' --include '*.py'| xargs sed -i '1s\^#!/usr/bin/env python$\\'

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-librosa
%doc README.md AUTHORS.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE.md
%{python2_sitelib}/librosa/
%{python2_sitelib}/librosa-%{version}-py%{python2_version}.egg-info

%files -n python3-librosa
%doc README.md AUTHORS.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE.md
%{python3_sitelib}/librosa/
%{python3_sitelib}/librosa-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Mar 18 2016 Dominika Krejci <dkrejci@redhat.com> - 0.4.2-1
- initial release