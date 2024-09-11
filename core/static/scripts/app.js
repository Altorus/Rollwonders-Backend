import { accordion } from "./modules/base/accordion.js";

import {preloader} from "./modules/preloader.js";
import {popup} from "./modules/popup.js";
import {themeManager} from "./modules/themeManager.js";
import * as pages from './modules/pages/index.js';
import {shareMenu} from "./modules/shareMenu.js";

preloader()
popup()
accordion()
themeManager()
shareMenu()