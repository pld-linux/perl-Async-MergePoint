#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Async
%define	pnam	MergePoint
Summary:	Async::MergePoint - resynchronise diverged control flow
Summary(pl.UTF-8):	Async::MergePoint - ponowna synchronizacja rozdzielonego sterowania
Name:		perl-Async-MergePoint
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/P/PE/PEVANS/Async-MergePoint-%{version}.tar.gz
# Source0-md5:	e9055c122e02fd75c8d604bb1dca49ca
URL:		http://search.cpan.org/dist/Async-MergePoint/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Exception
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Often in program logic, multiple different steps need to be taken that
are independent of each other, but their total result is needed before
the next step can be taken. In synchonous code, the usual approach is
to do them sequentially.

An asynchronous or event-based program could do this, but if each step
involves some IO idle time, better overall performance can often be
gained by running the steps in parallel. A Async::MergePoint object
can then be used to wait for all of the steps to complete, before
passing the combined result of each step on to the next stage.

%description -l pl.UTF-8
Często w logice programu trzeba wykonać kilka czynności niezależnych
od siebie, ale ich łączny wynik jest potrzebny przed przejściem do
następnego kroku. W kodzie synchronicznym zwykle wykonuje się je
sekwencyjnie.

W programie asynchronicznym lub sterowanym zdarzeniami można zrobić
tak samo, ale jeśli każdy z kroków obejmuje jakiś czas bezczynności
we/wy, lepszą wydajność całkowitą osiąga się wykonując czynności
równolegle. W takim wypadku można wykorzystać obiekt Async::MergePoint
w celu zaczekania na wykonanie wszystkich czynności przed przekazaniem
wyniku do następnego etapu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Async
%{perl_vendorlib}/Async/MergePoint.pm
%{_mandir}/man3/Async::MergePoint.3pm*
