%define	pdir	Tk
%define	pnam	WaitBox
%include	/usr/lib/rpm/macros.perl
Summary:	Tk-WaitBox perl module
Summary(pl):	Modu³ perla Tk-WaitBox
Name:		perl-Tk-WaitBox
Version:	1.3
Release:	5

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk-WaitBox perl module.

%description -l pl
Modu³ perla Tk-WaitBox.

%prep
%setup -q -n Tk-WaitBox-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Tk/WaitBox.pm
%{_mandir}/man3/*
