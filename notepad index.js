const gplay = require('google-play-scraper');

gplay.app({ appId: 'com.revolut.revolut' })  // Example app
  .then(app => {
    console.log('📱 App Title:', app.title);
    console.log('👨‍💻 Developer:', app.developer);
    console.log('⭐ Rating:', app.score);
    console.log('⬇️ Installs:', app.installs);
    console.log('📝 Summary:', app.summary);
  })
  .catch(err => {
    console.error('❌ Error fetching app data:', err);
  });
