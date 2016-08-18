
// pip install sru using --process-dependency-links
// dependency: sru_utils, sru_pip, sru_service, aiohttp
// cmd python sru.support.service -a setup -i sru -n SRU -d "desc" -e python 
//      -p "--port 30080 --host localhost --certFile ;; --certKey ;;"
// cmd python sru.support.service -a start
// service should now be started and running