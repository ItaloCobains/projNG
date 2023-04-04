(() => {
    const authorsLogoutLinks = document.querySelectorAll('.authors-logout-link');
    const formLogout = document.querySelector('.form-logout');
  
    for (const link of authorsLogoutLinks) {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        formLogout.submit();
      });
    }
})();