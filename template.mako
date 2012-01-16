<!doctype html>


<%! import markdown %>
<%def name="slide(id, attr, text)">
   <div id="${id}" class="step" ${attr}>
      ${ text }
   </div>
</%def>

<%def name="impress()">
   <div id="impress">
      <div class="no-support-message" style="font-size: x-large;font-weight: bolder">
          Your browser doesn't support impress.js.  Try Chrome or Safari.
      </div>

      ${caller.body()}

   </div>
   <!--<script type="text/javascript" src="https://raw.github.com/bartaz/impress.js/master/js/impress.js"></script>-->
   <script type="text/javascript" src="impress.js"></script>
</%def>




<%def name="document(style, slides)">
<html>
    <head>
        <title>Impress Tutorial</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

      <style type='text/css'>
         @import url('slideshow.css');

         .no-support-message { display:none; }
         .impress-not-supported .no-support-message { display:block; }

         ${style}

      </style>
    </head>
    <body>

   <%self:impress>
      %for slide in slides:
         ${slide}
      %endfor
   </%self:impress>


    </body>
</html>
</%def>

