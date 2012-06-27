%global project   felix-gogo
%global pkgname   parent

Name:             %{project}-%{pkgname}
Version:          0.6.0
Release:          1
Summary:          Parent package for Felix Gogo
Group:            Development/Java
License:          ASL 2.0
URL:              http://felix.apache.org/site/apache-felix-gogo.html

Source0:          http://apache.mirror.rbftpnetworks.com//felix/gogo-parent-0.6.0-project.tar.gz

BuildArch:        noarch

BuildRequires:    java
BuildRequires:    maven
BuildRequires:    jpackage-utils

Requires:         java 
BuildRequires:    maven
Requires:         jpackage-utils

%description
Apache Felix is a community effort to implement the OSGi R4 Service Platform
and other interesting OSGi-related technologies under the Apache license. The
OSGi specifications originally targeted embedded devices and home services
gateways, but they are ideally suited for any project interested in the
principles of modularity, component-orientation, and/or service-orientation.
OSGi technology combines aspects of these aforementioned principles to define a
dynamic service deployment framework that is amenable to remote management.

%prep
%setup -q -n gogo-parent-%{version}

%build
mvn-rpmbuild install

%install
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom 


%files
%doc LICENSE NOTICE
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

