import React from "react";

import img1 from "../../img/img1.jpg";
import img2 from "../../img/img2.jpg";
import img3 from "../../img/img3.jpg";
import img4 from "../../img/img4.jpg";
import img5 from "../../img/img5.jpg";
import img6 from "../../img/img6.jpg";

export default function PreviewImg(): React.JSX.Element {
  return (
    <div className="w-full overflow-x-scroll">
      <div className="flex whitespace-nowrap">
        <div className="flex">
          <img src={img1} className="w-64 m-12 rounded-[35px] shadow-2xl shadow-stone-600" />
          <img src={img2} className="w-64 m-12 rounded-[35px] shadow-2xl shadow-stone-600" />
          <img src={img3} className="w-64 m-12 rounded-[35px] shadow-2xl shadow-stone-600" />
          <img src={img4} className="w-64 m-12 rounded-[35px] shadow-2xl shadow-stone-600" />
          <img src={img5} className="w-64 m-12 rounded-[35px] shadow-2xl shadow-stone-600" />
          <img src={img6} className="w-64 m-12 rounded-[35px] shadow-2xl shadow-stone-600" />
        </div>
      </div>
    </div>
  );
}
