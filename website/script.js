import { Html5Qrcode, Html5QrcodeScanner } from "html5-qrcode";

function QRScanner() {
    const scanner = new Html5QrcodeScanner("reader", { fps: 20 });
    scanner.render((result) => {
        console.log(result);
        scanner.clear();
    });
}

window.QRScanner = QRScanner;
