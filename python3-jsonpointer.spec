#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Identify specific nodes in a JSON document (RFC 6901)
Summary(pl.UTF-8):	Identyfikowanie określonych węzłów w dokumencie JSON (RFC 6901)
Name:		python3-jsonpointer
Version:	3.0.0
Release:	4
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jsonpointer/
Source0:	https://files.pythonhosted.org/packages/source/j/jsonpointer/jsonpointer-%{version}.tar.gz
# Source0-md5:	9a0b3e940bbd65f544f41018a904991f
URL:		https://pypi.org/project/jsonpointer/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
Provides:	jsonpointer = %{version}-%{release}
Obsoletes:	jsonpointer < 3.0.0-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to resolve JSON Pointers according to RFC 6901.

%description -l pl.UTF-8
Biblioteka do rozwiązywania wskaźników JSON zgodnie z RFC 6901.

%prep
%setup -q -n jsonpointer-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m unittest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/jsonpointer{,-3}
ln -sf jsonpointer-3 $RPM_BUILD_ROOT%{_bindir}/jsonpointer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE.txt README.md
%attr(755,root,root) %{_bindir}/jsonpointer
%attr(755,root,root) %{_bindir}/jsonpointer-3
%{py3_sitescriptdir}/jsonpointer.py
%{py3_sitescriptdir}/__pycache__/jsonpointer.cpython-*.py[co]
%{py3_sitescriptdir}/jsonpointer-%{version}-py*.egg-info
