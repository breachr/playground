const routes = [{
  path: '/',
  component: () => import('layouts/layout'),
  children: [{
    path: '',
    component: () => import('pages/page1/page1')
  }]
},

{
  path: '/banane/',
  component: () => import('layouts/layout'),
  children: [{
    path: '',
    component: () => import('pages/page1/page1')
  }]
},

{
  path: '/PAGE2/',
  component: () => import('layouts/layout'),
  children: [{
    path: '',
    component: () => import('pages/page2/page2')
  }]
},

{
  path: '/PAGE3/',
  component: () => import('layouts/layout'),
  children: [{
    path: '',
    component: () => import('pages/page3/page3')
  }]
}
]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/X_error/404.vue')
  })
}

export default routes
