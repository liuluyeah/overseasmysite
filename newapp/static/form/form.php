<?php

define('EMAIL_FOR_REPORTS', '');
define('RECAPTCHA_PRIVATE_KEY', '@privatekey@');
define('FINISH_URI', 'http://');
define('FINISH_ACTION', 'message');
define('FINISH_MESSAGE', 'Thanks for filling out my form!');
define('UPLOAD_ALLOWED_FILE_TYPES', 'doc, docx, xls, csv, txt, rtf, html, zip, jpg, jpeg, png, gif');

define('_DIR_', str_replace('\\', '/', dirname(__FILE__)) . '/');
require_once _DIR_ . '/handler.php';

?>

<?php if (frmd_message()): ?>
<link rel="stylesheet" href="<?php echo dirname($form_path); ?>/formoid-solid-green.css" type="text/css" />
<span class="alert alert-success"><?php echo FINISH_MESSAGE; ?></span>
<?php else: ?>
<!-- Start Formoid form-->
<link rel="stylesheet" href="<?php echo dirname($form_path); ?>/formoid-solid-green.css" type="text/css" />
<script type="text/javascript" src="<?php echo dirname($form_path); ?>/jquery.min.js"></script>
<form class="formoid-solid-green" style="background-color:#FFFFFF;font-size:16px;font-family:'Roboto',Arial,Helvetica,sans-serif;color:#34495E;max-width:480px;min-width:150px" method="post"><div class="title"><h2>Preliminary Assessment</h2></div>
	<div class="element-separator"><hr><h3 class="section-break-title">Basic information</h3></div>
	<div class="element-name<?php frmd_add_class("name1"); ?>"><label class="title"></label><span class="nameFirst"><input placeholder="Name First" type="text" size="8" name="name1[first]" /><span class="icon-place"></span></span><span class="nameLast"><input placeholder="Name Last" type="text" size="14" name="name1[last]" /><span class="icon-place"></span></span></div>
	<div class="element-phone<?php frmd_add_class("phone"); ?>"><label class="title"><span class="required">*</span></label><div class="item-cont"><input class="large" type="tel" pattern="[+]?[\.\s\-\(\)\*\#0-9]{3,}" maxlength="24" name="phone" required="required" placeholder="Phone" value=""/><span class="icon-place"></span></div></div>
	<div class="element-separator"><hr><h3 class="section-break-title">Intention country and major</h3></div>
	<div class="element-select<?php frmd_add_class("select"); ?>"><label class="title"><span class="required">*</span></label><div class="item-cont"><div class="large"><span><select name="select" required="required">

		<option value="USA">USA</option></select><i></i><span class="icon-place"></span></span></div></div></div>
	<div class="element-select<?php frmd_add_class("select1"); ?>"><label class="title"><span class="required">*</span></label><div class="item-cont"><div class="large"><span><select name="select1" required="required">

		<option value="EE">EE</option>
		<option value="CS">CS</option></select><i></i><span class="icon-place"></span></span></div></div></div>
	<div class="element-separator"><hr><h3 class="section-break-title">Education history</h3></div>
	<div class="element-select<?php frmd_add_class("select2"); ?>"><label class="title"><span class="required">*</span></label><div class="item-cont"><div class="large"><span><select name="select2" required="required">

		<option value="Peking University">Peking University</option></select><i></i><span class="icon-place"></span></span></div></div></div>
	<div class="element-input<?php frmd_add_class("input2"); ?>" title="66"><label class="title"><span class="required">*</span></label><div class="item-cont"><input class="medium" type="text" name="input2" required="required" placeholder="GPA"/><span class="icon-place"></span></div></div>
	<div class="element-input<?php frmd_add_class("input3"); ?>"><label class="title"><span class="required">*</span></label><div class="item-cont"><input class="medium" type="text" name="input3" required="required" placeholder="IELTS/TOEFL"/><span class="icon-place"></span></div></div>
	<div class="element-checkbox<?php frmd_add_class("checkbox"); ?>"><label class="title">Paper</label>		<div class="column column1"><label><input type="checkbox" name="checkbox[]" value="Science"/ ><span>Science</span></label><label><input type="checkbox" name="checkbox[]" value="Nature"/ ><span>Nature</span></label><label><input type="checkbox" name="checkbox[]" value="IEEE"/ ><span>IEEE</span></label><label><input type="checkbox" name="checkbox[]" value="SCI"/ ><span>SCI</span></label><label><input type="checkbox" name="checkbox[]" value="EI"/ ><span>EI</span></label><label><input type="checkbox" name="checkbox[]" value="others"/ ><span>others</span></label></div><span class="clearfix"></span>
</div>
	<div class="element-input<?php frmd_add_class("input4"); ?>"><label class="title"></label><div class="item-cont"><input class="medium" type="text" name="input4" placeholder="GRE"/><span class="icon-place"></span></div></div>
	<div class="element-input<?php frmd_add_class("input6"); ?>"><label class="title"></label><div class="item-cont"><input class="large" type="text" name="input6" placeholder="Patent"/><span class="icon-place"></span></div></div>
	<div class="element-input<?php frmd_add_class("input7"); ?>"><label class="title"></label><div class="item-cont"><input class="large" type="text" name="input7" placeholder="Research"/><span class="icon-place"></span></div></div>
	<div class="element-input<?php frmd_add_class("input8"); ?>"><label class="title"></label><div class="item-cont"><input class="large" type="text" name="input8" placeholder="Placement"/><span class="icon-place"></span></div></div>
	<div class="element-input<?php frmd_add_class("input9"); ?>"><label class="title"></label><div class="item-cont"><input class="large" type="text" name="input9" placeholder="Social Practice"/><span class="icon-place"></span></div></div>
	<div class="element-input<?php frmd_add_class("input11"); ?>"><label class="title"></label><div class="item-cont"><input class="large" type="text" name="input11" placeholder="Specialty"/><span class="icon-place"></span></div></div>
	<div class="element-input<?php frmd_add_class("input10"); ?>"><label class="title"></label><div class="item-cont"><input class="large" type="text" name="input10" placeholder="Recommendation Letter"/><span class="icon-place"></span></div></div>
<div class="submit"><input type="submit" value="Submit"/></div></form><script type="text/javascript" src="<?php echo dirname($form_path); ?>/formoid-solid-green.js"></script>

<!-- Stop Formoid form-->
<?php endif; ?>

<?php frmd_end_form(); ?>