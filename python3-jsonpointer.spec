#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

Summary:	Identify specific nodes in a JSON document (RFC 6901)
Summary(pl.UTF-8):	Identyfikowanie określonych węzłów w dokumencie JSON (RFC 6901)
Name:		python3-jsonpointer
Version:	3.0.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jsonpointer/
Source0:	https://files.pythonhosted.org/packages/source/j/jsonpointer/jsonpointer-%{version}.tar.gz
# Source0-md5:	9a0b3e940bbd65f544f41018a904991f
URL:		https://pypi.org/project/jsonpointer/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
Requires:	python-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to resolve JSON Pointers according to RFC 6901.

%description -l pl.UTF-8
Biblioteka do rozwiązywania wskaźników JSON zgodnie z RFC 6901.

%package -n jsonpointer
Summary:	Identify specific nodes in a JSON document (RFC 6901)
Summary(pl.UTF-8):	Identyfikowanie określonych węzłów w dokumencie JSON (RFC 6901)
Group:		Applications/Text
Requires:	python3-jsonpointer = %{version}-%{release}

%description -n jsonpointer
Tool to resolve JSON Pointers according to RFC 6901.

%description -n jsonpointer -l pl.UTF-8
Narzędzie do rozwiązywania wskaźników JSON zgodnie z RFC 6901.

%prep
%setup -q -n jsonpointer-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} tests.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE.txt README.md
%{py3_sitescriptdir}/jsonpointer.py
%{py3_sitescriptdir}/__pycache__/jsonpointer.cpython-*.py[co]
%{py3_sitescriptdir}/jsonpointer-%{version}-py*.egg-info

%files -n jsonpointer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jsonpointer
