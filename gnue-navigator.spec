Summary:	GNUe Navigator - a menuing system for GNUe Forms and Reports
#Summary(pl):	
Name:		gnue-navigator
Version:	0.0.8
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.gnuenterprise.org/downloads/current/%{name}-%{version}.tar.gz
# Source0-md5:	582722837c31d1cd368423eed6e37b05
URL:		http://www.gnuenterprise.org/
BuildRequires:	gnue-common
BuildRequires:	gnue-forms
BuildRequires:	gnue-reports
BuildRequires:	python
BuildRequires:	python-devel
Requires:	gnue-common
Requires:	gnue-forms
Requires:	gnue-reports
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNUe Navigator is a menuing system for GNUe Forms and Reports.
It presents a consistent menuing interface (in GUI or Text) based
on an XML "process definition."  GNUe Navigator uses the GNUe
Forms or GNUe Reports clients to run the actual forms and reports,
so these corresponding tools must be installed.

#%description -l pl

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

cp -a samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README* TODO doc/*.* doc/technotes
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/gnue/navigator
%{_mandir}/man?/*
%{_examplesdir}/%{name}-%{version}
