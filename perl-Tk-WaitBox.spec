%include	/usr/lib/rpm/macros.perl
Summary:	Tk-WaitBox perl module
Summary(pl):	Modu³ perla Tk-WaitBox
Name:		perl-Tk-WaitBox
Version:	1.3
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tk/Tk-WaitBox-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Tk
%requires_eq	perl
Requires:	%{perl_sitearch}
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

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Tk/WaitBox
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv -f .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Tk/WaitBox.pm
%{perl_sitearch}/auto/Tk/WaitBox

%{_mandir}/man3/*
