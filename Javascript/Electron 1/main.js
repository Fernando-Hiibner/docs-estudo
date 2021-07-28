const {app, BrowserWindow, Menu, MenuItem, globalShortcut} = require('electron');
const fs = require('fs');
const path = require('path');

// app.setUserTasks([
//     {
//       program: process.execPath,
//       arguments: '--new-window',
//       iconPath: process.execPath,
//       iconIndex: 0,
//       title: 'New Window',
//       description: 'Create a new window'
//     }
//   ])

app.setUserTasks([]);

const menu = new Menu()
menu.append(new MenuItem({
  label: 'Electron',
  submenu: [{
    role: 'help',
    accelerator: process.platform === 'darwin' ? 'Alt+Cmd+I' : 'Alt+Shift+I',
    click: () => { console.log('Electron rocks!') }
  }]
}))
menu.append(new MenuItem({
  label: 'Baozi',
  submenu: [{
      label:"Baozi",
      role: 'toggleDevTools',
      accelerator: process.platform === 'darwin' ? 'Ctrl+Cmd+I' : 'Ctrl+Shift+I',
  }]
}))

Menu.setApplicationMenu(menu);
// Menu.setApplicationMenu(undefined);

let progressInterval;

function createWindow() {
    const win = new BrowserWindow({
        width : 800,
        height : 600,

        webPreferences : {
            preload : path.join(__dirname, 'preload.js')
        }
    });

    // win.loadURL('https://www.electronjs.org/docs/tutorial/quick-start');
    win.loadFile('index.html');

    const INCREMENT = 0.03;
    const INCREMENT_DELAY = 100;

    let c = 0;
    progressInterval = setInterval(() => {
        win.setProgressBar(c);

        if(c < 2){
            c += INCREMENT;
        }
        else{
            c = 0;
        }
    }, INCREMENT_DELAY);

    win.setThumbarButtons([
        {
          tooltip: 'button1',
          icon: path.join(__dirname, 'button1.png'),
          click () { console.log('button1 clicked') }
        }, {
          tooltip: 'button2',
          icon: path.join(__dirname, 'button2.png'),
          flags: ['enabled', 'dismissonclick'],
          click () { console.log('button2 clicked.') }
        }
      ]);

    win.setOverlayIcon('./button1.png', 'Description for overlay')

}

const fileName = 'recently-used.md';
fs.writeFile(fileName, 'Baozi Grande?', () => {
    app.addRecentDocument(path.join(__dirname, fileName));
});

app.whenReady().then(() => {
    globalShortcut.register('Alt+CommandOrControl+O', () => {
        console.log("Baoziiii");
    });
}).then(createWindow);

app.on('before-quit', () => {
    clearInterval(progressInterval);
})

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
})

app.on('window-all-closed', () => {
    app.clearRecentDocuments();
    if (process.platform !== 'darwin') {
        app.quit();
    }
});