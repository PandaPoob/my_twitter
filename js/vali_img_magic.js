function validateImageMagicType(file) {
  return new Promise((resolve, reject) => {
    //Using HTML5 File API
    const reader = new FileReader();

    reader.onloadend = function () {
      const arr = new Uint8Array(reader.result).subarray(0, 4);
      let header = "";

      for (let i = 0; i < arr.length; i++) {
        header += arr[i].toString(16);
      }

      let imageType = "";

      switch (header) {
        case "89504e47":
          imageType = "image/png";
          break;
        case "ffd8ffe0":
        case "ffd8ffe1":
        case "ffd8ffe2":
          imageType = "image/jpeg";
          break;
        default:
          imageType = "unknown";
          break;
      }
      resolve(imageType);
    };

    reader.onerror = function () {
      reject(new Error("Error reading file."));
    };

    reader.readAsArrayBuffer(file);
  });
}
