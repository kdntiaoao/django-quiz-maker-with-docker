const menuBtn = document.querySelector('.js-menu-btn')
const menuNav = document.querySelector('.js-menu-nav')
const headerSubEl = document.querySelector('.js-header-sub')

menuBtn.addEventListener('click', (ev) => {
  const target = ev.currentTarget
  if (target.getAttribute('aria-expanded') === 'false') {
    target.setAttribute('aria-expanded', 'true')
    target.setAttribute('aria-label', 'メニューを閉じる')
    menuNav.classList.add('is-shown')
    menuNav.classList.remove('is-hidden')
    headerSubEl.classList.add('is-shown')
    headerSubEl.classList.remove('is-hidden')
    document.body.classList.add('u-fixed')
  } else {
    target.setAttribute('aria-expanded', 'false')
    target.setAttribute('aria-label', 'メニューを開く')
    menuNav.classList.remove('is-shown')
    menuNav.classList.add('is-hidden')
    headerSubEl.classList.remove('is-shown')
    headerSubEl.classList.add('is-hidden')
    document.body.classList.remove('u-fixed')
  }
})
