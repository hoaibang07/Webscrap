using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Net;
using System.IO;

namespace CRWeb
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            txtLink.Text = @"http://api.mp3.zing.vn/api/mobile/song/getsonginfo?requestdata={""id"":""IDBAIHAT""}";
        }

        private void btnResetUrl_Click(object sender, EventArgs e)
        {
            txtLink.Text = @"http://api.mp3.zing.vn/api/mobile/song/getsonginfo?requestdata={""id"":""IDBAIHAT""}";
        }

        private void btnGetHTMLSource_Click(object sender, EventArgs e)
        {
            string urlAddress = txtLink.Text;

            //Method 1: Using request(if site check request, cannot using this.)

            //HttpWebRequest request = (HttpWebRequest)WebRequest.Create(urlAddress);
            //HttpWebResponse response = (HttpWebResponse)request.GetResponse();

            //if (response.StatusCode == HttpStatusCode.OK)
            //{
            //    Stream receiveStream = response.GetResponseStream();
            //    StreamReader readStream = null;

            //    if (response.CharacterSet == null)
            //    {
            //        readStream = new StreamReader(receiveStream);
            //    }
            //    else
            //    {
            //        readStream = new StreamReader(receiveStream, Encoding.GetEncoding(response.CharacterSet));
            //    }

            //    string data = readStream.ReadToEnd();
            //    rtbResult.Text = data;

            //    response.Close();
            //    readStream.Close();
            //}

            //Method 2: Using webclient
            using (WebClient client = new WebClient())
            {
                string htmlCode = client.DownloadString(urlAddress);
                rtbResult.Text = htmlCode;
            }
        }
     }
}
